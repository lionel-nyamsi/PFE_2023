package cm.pfe2023.li_ionassist

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class ConnectionActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_connection)

        var connection_btn = findViewById<Button>(R.id.connection_btn)
        connection_btn.setOnClickListener {
            nextPage()
        }
    }

    private fun nextPage() {
        val scan_page = Intent(this, ScanCodeActivity()::class.java)
        startActivity(scan_page)
    }
}