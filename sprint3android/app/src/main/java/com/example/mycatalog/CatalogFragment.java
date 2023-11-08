package com.example.mycatalog;

import android.os.Bundle;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class CatalogFragment extends Fragment {
    private Button button;
    private Fragment fragment;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_catalog, container, false);
        button = view.findViewById(R.id.detalle); /*Aqui declaramos el boton con el id del xml*/
        button.setOnClickListener(new View.OnClickListener() { /*Aqui decimos que escuche si se pulsa el boton*/
            @Override
            public void onClick(View view) { /*Aqui decimos que al clickar el boton haga...*/
                fragment = new DetailFragment(); /*Aqui decimos que navegue al DetailFragment*/
                FragmentManager fragmentManager = requireActivity().getSupportFragmentManager(); /*Aqui decimos que el fragment manager es el que gestiona los fragmentos*/
                FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
                fragmentTransaction.replace(R.id.contenedor, fragment); // Reemplaza el fragmento actual por el nuevo
                fragmentTransaction.addToBackStack(null); // Hace que el fragmento reemplazado se guarde en la pila de retroceso
                fragmentTransaction.commit(); // Aplicas el fragmento
            }
        });
        return view;
    }
}