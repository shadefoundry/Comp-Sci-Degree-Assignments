package com.shadefoundry.assignment3;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

/**
 * Created by link491 on 11/17/2016.
 */
public class MissionDB {

    private Context context;
    //define sqlite open helper and database
    private SQLiteOpenHelper openHelper;
    private SQLiteDatabase database;

    //context for database
    public MissionDB(Context context) {
        this.context = context;
        openHelper = new MyOpenHelper(context);

    }

    //define table pieces
    private final static String TABLE_NAME = "missions";
    private final  String DATABASE_NAME = "missions.db";
    private final static int DATABASE_VERSION = 1;

    //declare table columns
    private final static String COLUMN_ID = "_id";
    private final static String COLUMN_PRIORITY = "priority";
    private final static String COLUMN_COMPLETED = "completed";
    private final static String COLUMN_MISSION = "mission";

    //actually create the table
    private final static String CREATE_TABLE =
            "CREATE TABLE " + TABLE_NAME +" ("+
                    COLUMN_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "+
                    COLUMN_PRIORITY+" INTEGER, "+
                    COLUMN_COMPLETED+" INTEGER, "+
                    COLUMN_MISSION+" TEXT)";

    //clear previous missions from database to avoid duplicates
    public int removeMissions(){
        database = openHelper.getWritableDatabase();

        int numRows = database.delete(TABLE_NAME,"1",null);

        database.close();

        return numRows;
    }

    public long saveMission(Mission mission) {
        /*Should save one row to the database*/
        ContentValues cv = new ContentValues();
        cv.put(COLUMN_PRIORITY, mission.getPriority());
        cv.put(COLUMN_MISSION, mission.getMission());
        cv.put(COLUMN_COMPLETED,0);

        database = openHelper.getWritableDatabase();
        long id = database.insert(TABLE_NAME,null,cv);
        database.close();
        return id;
    }

    public Mission getNextMission(){
        String selection =COLUMN_COMPLETED+"=?";
        String[] selectionArgs = {"0"};

        database=openHelper.getReadableDatabase();

        Cursor cursor= database.query(TABLE_NAME,null,selection,selectionArgs,null,null,COLUMN_PRIORITY);

        Mission mission = null;

        if(cursor.moveToNext()){
            long id = cursor.getLong(cursor.getColumnIndex(COLUMN_ID));
            long priority = cursor.getLong(cursor.getColumnIndex(COLUMN_PRIORITY));
            String missionText = cursor.getString(cursor.getColumnIndex(COLUMN_MISSION));

            mission = new Mission(id,priority,missionText);
        }
        database.close();
        return mission;
    }

    public int setMissionCompleter(Mission mission){
        ContentValues cv = new ContentValues();

        //use an inline if here
        cv.put(COLUMN_COMPLETED,mission.isCompleted()?1:0);

        String where = COLUMN_ID + " = ?";

        //creating a array of one element
        String[] whereArguments = new String[]{String.valueOf(mission.get_id())};

        //call open helper to get writeable database
        database = openHelper.getWritableDatabase();

        int numRows = database.update(TABLE_NAME,cv,where,whereArguments);
        database.close();
        return numRows;
    }

    //define MyOpenHelper for database itself
    private class MyOpenHelper extends SQLiteOpenHelper{
        public MyOpenHelper(Context context) {
            super(context, DATABASE_NAME, null,DATABASE_VERSION);
        }

        @Override
        public void onCreate(SQLiteDatabase db){
            db.execSQL(CREATE_TABLE);
        }
        //go about upgrading the database
        // basically we drop it if it exists and then create a new one
        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion){
            db.execSQL("DROP TABLE IF EXISTS" + TABLE_NAME);
            onCreate(db);
        }
    }
}
