package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class RecycleViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;
    private RecyclerViewData data;

    public RecycleViewHolder(@NonNull View itemView) {
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.vista_texto);
        imageView = (ImageView) itemView.findViewById(R.id.vista_imagen);

        //Aqui hacemos que detecte si clickan en la imagen y nos lleve a la activity de detalle
        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            // Aqui decimos que cuando clicken haga algo
            public void onClick(View v) {
                String name = data.getName();
                Context context = v.getContext();
                // Aqui le decimos que nos lleve a la DetailActivity
                Intent intent = new Intent(context, DetailActivity.class);
                intent.putExtra("titulo", name);
                intent.putExtra("imagen", data.getImageUrl());
                intent.putExtra("descripcion", data.getDescription());
                context.startActivity(intent);
            }
        });
    }

    //metodo que muestra la informacion en la celda
    public void showData(RecyclerViewData data, Activity activity) {
        this.data = data; // Initialize the data object
        textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into(imageView);
    }
}
