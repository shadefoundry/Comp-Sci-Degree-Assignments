package com.shadefoundry.assignment3;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MissionActivity extends AppCompatActivity {
    Mission mission;
    /*On create we...
    * Get the intent
    * set the UI text to the current mission*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mission);

        Intent intent = getIntent();

        mission = intent.getParcelableExtra("mission");

        TextView txtMission =(TextView) findViewById(R.id.txtMission);

        txtMission.setText(mission.getMission());
    }

    public static final String MISSION_COMPLETED = "missionCompleted";

    public void missionCompleted(View view) {

        mission.setCompleted(true);

        //create a broadcast to tell mission complete
        Intent intent = new Intent();
        intent.putExtra("mission",mission);
        intent.setAction(MISSION_COMPLETED);
        sendBroadcast(intent);
        finish();
    }
}
