package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    /*Aqui inicializamos las variables*/
    private Button button;
    private Context context=this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog); /*Aqui declaramos el xml del layout*/
        button = findViewById(R.id.detalle); /*Aqui declaramos el boton con el id del xml*/
        button.setOnClickListener(new View.OnClickListener() { /*Aqui decimos que escuche si se pulsa el boton*/
            @Override
            public void onClick(View view) { /*Aqui decimos que al clickar el boton haga...*/
                Intent intent = new Intent(context, DetailActivity.class); /*Aqui creamos un intento de cargar otra empty activity*/
                context.startActivity(intent); /*Aqui lanzamos la otra empty activity*/
            }
        });
    }
}