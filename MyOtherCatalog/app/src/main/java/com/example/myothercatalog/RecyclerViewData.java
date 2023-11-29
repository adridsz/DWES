package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;
public class RecyclerViewData {
    private String name;
    private String imageUrl;
    private String description;

    public RecyclerViewData(JSONObject json) { //recibe un json
        //parseo el json
        try{
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
            this.description = json.getString("description");
        }catch (JSONException e) {
            e.printStackTrace();
        }
    }

    //getters
    public String getName() {
        return name;
    }
    public String getImageUrl() {
        return imageUrl;
    }

    public String getDescription() {
        return description;
    }
}