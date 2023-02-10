package cm.pfe2023.li_ionassist

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.CountDownTimer

class ScanCodeActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_scan_code)

    }


    private fun nextPage() {
        val connection_succesful_page = Intent(this, ConnectionSuccesfulActivity()::class.java)
        startActivity(connection_succesful_page)
    }

}