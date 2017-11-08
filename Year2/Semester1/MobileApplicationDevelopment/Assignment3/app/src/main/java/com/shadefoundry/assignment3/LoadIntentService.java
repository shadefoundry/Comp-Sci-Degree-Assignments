package com.shadefoundry.assignment3;

import android.app.IntentService;
import android.content.Intent;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

/**
 * Created by Kevin Lopez on 11/17/2016.
 */
public class LoadIntentService  extends IntentService{
    /**
     * Creates an IntentService.  Invoked by your subclass's constructor.
     *
     */
    public LoadIntentService() {
        super("LoadIntentService");
    }

    public static String LOAD_SUCCESS="Load Success";
    public static String LOAD_BROADCAST="Load Broadcast";

    @Override
    protected void onHandleIntent(Intent intent) {

        //get the file
        URL url;
        InputStream is = null;

        try {
            url = new URL("http://mobile.sheridanc.on.ca/~bonenfan/PROG20146/missions.txt");

            URLConnection conn = url.openConnection();

            HttpURLConnection httpconn = (HttpURLConnection) conn;

            int responseCode = httpconn.getResponseCode();
            //if we got the file, create the Mission Database
            if(responseCode == HttpURLConnection.HTTP_OK){
                MissionDB missionDB = new MissionDB(this);

                missionDB.removeMissions();

                is = httpconn.getInputStream();

                Scanner scanner = new Scanner(is);
                while(scanner.hasNextLine()){
                    String lineIn = scanner.nextLine();
                    Mission mission = new Mission(lineIn);
                    missionDB.saveMission(mission);
                }

                Intent broadcastIntent = new Intent();
                broadcastIntent.putExtra(LOAD_SUCCESS,true);
                broadcastIntent.setAction(LOAD_BROADCAST);

                sendBroadcast(broadcastIntent);

            }
            //catch any exceptions and disregard them because
            // unless the text file doesn't exist, we'll never see them.
        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            if(is != null){
                try {
                    is.close();
                } catch (IOException ignored) {}
            }
        }

    }
}
