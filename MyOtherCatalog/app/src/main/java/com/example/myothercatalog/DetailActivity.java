package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {
    private TextView titulo;
    private ImageView imagen;
    private TextView descripcion;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
        // Aqui recogemos los datos que nos envia la MainActivity
        Intent intent = getIntent();
        String tittle = intent.getStringExtra("titulo");
        String Image = intent.getStringExtra("imagen");
        String Description = intent.getStringExtra("descripcion");
        // Aqui llamamos al metodo verDatos para que nos muestre los datos
        verDatos(tittle, Image, Description);
    }

    private void verDatos(String tittle, String Image, String Description) {
        //Aqui inicializamos los elementos
        titulo = findViewById(R.id.titulo);
        CardView cardView = findViewById(R.id.imagen);
        imagen = cardView.findViewById(R.id.imageview);
        descripcion = findViewById(R.id.descripcion);
        //Aqui le decimos que nos muestre los datos
        titulo.setText(tittle);
        Glide.with(this).load(Image).into(imagen);
        descripcion.setText(Description);
    }
}