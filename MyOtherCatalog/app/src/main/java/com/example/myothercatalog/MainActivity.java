package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.widget.Toast;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
        private Context context;
        private RequestQueue requestQueue;
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            context = this;
            requestQueue = Volley.newRequestQueue(this);

            Toast.makeText(this, "Cargando", Toast.LENGTH_LONG).show();
            showRecyclerView();
        }




        //En este metodo se hace la peticion y se muestra la lista
        private void showRecyclerView() {
            RecyclerView recyclerView = findViewById(R.id.recycler_view);
            Activity activity = this;

            context = this;

            //Creamos el jsonarray ya que la informacion q queremos mostrar esta en un jsonarray
            JsonArrayRequest request = new JsonArrayRequest(
                    Request.Method.GET,
                    "https://raw.githubusercontent.com/adridsz/DWES/main/recursos/catalog.json", //La url de mi catalog para que descargue la informacion
                    null,
                    new Response.Listener<JSONArray>() { //Si la peticion es correcta realiza esta acción
                        @Override
                        public void onResponse(JSONArray response) {
                            List<RecyclerViewData> allThelandscapes = new ArrayList<>(); // Creo la lista para almacenar los datos
                            for (int i=0; i< response.length(); i++) { //Recorro el jsonarray
                                try{
                                    JSONObject landscape = response.getJSONObject(i); //Obtengo el objeto json
                                    RecyclerViewData data = new RecyclerViewData(landscape); //Creo un objeto de la clase RecyclerViewData
                                    allThelandscapes.add(data); //Añado el objeto a la lista
                                }catch (JSONException e) {
                                    e.printStackTrace();
                                }
                            }
                            RecyclerViewAdapter adapter = new RecyclerViewAdapter(allThelandscapes, activity);
                            recyclerView.setAdapter(adapter);
                            recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                        }
                    },
                    new Response.ErrorListener() { //si la peticion falla realiza esta accion
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    }
            );
            this.requestQueue.add(request);
        }
    }