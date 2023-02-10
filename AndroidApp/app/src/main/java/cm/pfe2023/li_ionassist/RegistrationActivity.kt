package cm.pfe2023.li_ionassist

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class RegistrationActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_registration)

        var summit_btn = findViewById<Button>(R.id.confirm_button)
        summit_btn.setOnClickListener {
            nextPage()
        }
    }

    private fun nextPage() {
        val connection_page = Intent(this, ConnectionActivity()::class.java)
        startActivity(connection_page)
    }
}