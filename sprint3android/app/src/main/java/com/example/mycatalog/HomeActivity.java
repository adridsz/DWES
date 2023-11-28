package com.example.mycatalog;

import androidx.activity.OnBackPressedCallback;
import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;
import android.content.Context;
import android.os.Bundle;
import android.view.MenuItem;

import com.google.android.material.navigation.NavigationView;

public class HomeActivity extends AppCompatActivity {
    private Context context = this;
    private DrawerLayout drawerLayout;
    private Toolbar toolbar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        toolbar = findViewById(R.id.toolbar);
        drawerLayout = findViewById(R.id.drawer_layout);

        // Metodo con el que cerramos el menu si se pulsa atrás.
        getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
            // Metodo con el que cerramos el menu si se pulsa atrás.
            @Override
            public void handleOnBackPressed() {
                if (drawerLayout.isDrawerOpen(GravityCompat.START)){
                    drawerLayout.closeDrawer(GravityCompat.START);
                }else{
                    if (isEnabled()){
                        setEnabled(false);
                        HomeActivity.super.onBackPressed();
                    }
                }
            }
        });
        setSupportActionBar(toolbar);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(new NavigationView.OnNavigationItemSelectedListener() { // Aqui creamos el menu que muestra las opiones
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                // Aqui hacemos que al cl   ickar a cierto item muestre un fragment
                Fragment fragment = null;
                if (item.getItemId() == R.id.catalogo) {
                    // Mostramos el CatalogFragment
                    fragment = new CatalogFragment();

                }else if(item.getItemId() == R.id.sobre_la_actividad){
                    // Mostramos el AboutFragment
                    fragment = new AboutFragment();
                }
                //Si clickas en una opcion del menu que no contenga ningun fragment, aqui hacemos que no se muestre nada más que el contenedor vacio
                if (fragment != null){
                    getSupportFragmentManager().beginTransaction().replace(R.id.contenedor, fragment).commit();
                    drawerLayout.closeDrawer(GravityCompat.START);
                    return true;
                }
                // Cerramos el Navigation Drawer después de la selección
                return false;

            }
        });
    }

}