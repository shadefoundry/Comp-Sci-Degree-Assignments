package com.shadefoundry.assignment3;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.common.api.GoogleApiClient;

public class MainActivity extends AppCompatActivity {

    //declare the UI elements
    private TextView txt_message;
    private Button btn_nextMission;

    private BroadcastReceiver reciever=new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            //if we successfully loaded the broadcast
            if(intent.getAction().equals(LoadIntentService.LOAD_SUCCESS)) {
                boolean success =
                        intent.getBooleanExtra(LoadIntentService.LOAD_SUCCESS, false);
                if (success) {
                    //give a toast and enable the button
                    Toast.makeText(MainActivity.this, "Success", Toast.LENGTH_SHORT).show();
                    btn_nextMission.setEnabled(true);
                }
            }
            //if mission is completed let the user know
            else if(intent.getAction().equals(MissionActivity.MISSION_COMPLETED)){
                Mission mission = intent.getParcelableExtra("mission");

                MissionDB missionDB = new MissionDB(MainActivity.this);

                int numRows = missionDB.setMissionCompleter(mission);

                if(numRows>0){
                    txt_message.setText("Mission completed: " + mission.getMission());
                }
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txt_message = (TextView) findViewById(R.id.txt_Message);
        btn_nextMission = (Button) findViewById(R.id.btn_nextMissions);

        IntentFilter loadFilter = new IntentFilter();
        loadFilter.addCategory(Intent.CATEGORY_DEFAULT);
        loadFilter.addAction(LoadIntentService.LOAD_BROADCAST);
        loadFilter.addAction(MissionActivity.MISSION_COMPLETED);

        registerReceiver(reciever,loadFilter);


    }
    //overridden because we have to. Not really ever changed
    @Override
    protected void onStop(){
        super.onStop();
    }

    //kill the reciever on destruction of app
    @Override
    protected void onDestroy(){
        unregisterReceiver(reciever);
        super.onDestroy();
    }

    /*This method...
    * -gets file through internet
    * -File IO
    * -Populate Database with a line from the file*/
    public void loadMissions(View view) {

        //check for internet connectivity
        ConnectivityManager cm = (ConnectivityManager) getSystemService(CONNECTIVITY_SERVICE);

        NetworkInfo ni = cm.getActiveNetworkInfo();

        //determine if we have a connection
        if (ni == null || !ni.isConnected()) {
            txt_message.setText("No network connection");
        } else {
            txt_message.setText("Network Connected");
            btn_nextMission.setEnabled(true);
            Intent intent = new Intent(this, LoadIntentService.class);
            startService(intent);
        }

    }

    private static int MY_NOTIFICATION = 1;

    public void nextMission(View view) {

        MissionDB missionDB = new MissionDB(this);
        Mission mission = missionDB.getNextMission();

        //if we have no more missions, let the user know
        if(mission==null){
            txt_message.setText("No more missions!");
            btn_nextMission.setEnabled(false);
            return;
        }

        Intent missionActivityIntent = new Intent(this,MissionActivity.class);

        missionActivityIntent.putExtra("mission",mission);

        int flag = PendingIntent.FLAG_UPDATE_CURRENT;

        PendingIntent pi = PendingIntent.getActivity(this, 0, missionActivityIntent,flag);

        //create a notification that gets the settings from a method
        Notification notification = getNotification(mission, pi);

        NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);

        nm.notify(MY_NOTIFICATION,notification);
    }

    //extracted notification creator.
    private Notification getNotification(Mission mission, PendingIntent pi) {
        return new Notification.Builder(this)
                    .setWhen(System.currentTimeMillis())
                    .setTicker("New Mission")
                    .setSmallIcon(R.mipmap.ic_launcher)
                    .setContentTitle("Your next mission will be")
                    .setContentText(mission.getMission())
                    .setContentIntent(pi)
                    .setAutoCancel(true)
                    .build();
    }
}
