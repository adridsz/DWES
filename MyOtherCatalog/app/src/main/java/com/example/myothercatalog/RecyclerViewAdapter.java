package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;
public class RecyclerViewAdapter extends RecyclerView.Adapter<RecycleViewHolder> {
    private List<RecyclerViewData> allTheData;
    private Activity activity;

    //Constructor que recibe la lista de datos a mostrar
    public RecyclerViewAdapter(List<RecyclerViewData> allTheData, Activity activity) {
        this.allTheData = allTheData;
        this.activity = activity;
    }

    @NonNull
    @Override
    //Aqui se crea la celda
    public RecycleViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.recycler_view_holder, parent, false);
        return new RecycleViewHolder(view); //aqui le paso la celda que cree
    }

    @Override
    //Aqui se le pasa la informacion a la celda
    public void onBindViewHolder(@NonNull RecycleViewHolder holder, int position) {
        RecyclerViewData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    @Override
    //Aqui se le dice cuantos elementos tiene la lista
    public int getItemCount() {
        return allTheData.size(); //devuelve el tamaño de la lista
    }
}