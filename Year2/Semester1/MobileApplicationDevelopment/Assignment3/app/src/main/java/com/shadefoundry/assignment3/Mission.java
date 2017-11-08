package com.shadefoundry.assignment3;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * Created by link491 on 11/17/2016.
 */
public class Mission implements Parcelable{
    private long _id;
    private long priority;
    private boolean completed;
    private String mission;

    public Mission(int priority, String mission) {
        this.priority = priority;
        this.mission = mission;
    }

    public Mission(String lineIn) {
        String[] splitLine = lineIn.split(",");
        this.priority = Integer.parseInt(splitLine[0]);
        this.mission = splitLine[1];

    }

    public Mission(long id, long priority, String missionText) {
        this._id = id;
        this.priority=priority;
        this.mission = missionText;
    }

    protected Mission(Parcel in) {
        _id = in.readLong();
        priority = in.readLong();
        completed = in.readByte() != 0;
        mission = in.readString();
    }

    //creates a new instance of mission to complete
    public static final Creator<Mission> CREATOR = new Creator<Mission>() {
        @Override
        public Mission createFromParcel(Parcel in) {
            return new Mission(in);
        }

        @Override
        public Mission[] newArray(int size) {
            return new Mission[size];
        }
    };

    public long get_id() {

        return _id;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    //exactly what it looks like, write to the parcelable
    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeLong(_id);
        dest.writeLong(priority);
        dest.writeByte((byte) (completed ? 1 : 0));
        dest.writeString(mission);
    }

    public void set_id(int _id) {
        this._id = _id;
    }

    public long getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public boolean isCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }

    public String getMission() {
        return mission;
    }

    public void setMission(String mission) {
        this.mission = mission;
    }
}
