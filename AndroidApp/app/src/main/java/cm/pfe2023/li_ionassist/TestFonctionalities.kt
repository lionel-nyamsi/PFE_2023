package cm.pfe2023.li_ionassist

import android.Manifest
import android.annotation.SuppressLint
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.telephony.SmsManager
import android.view.WindowInsetsAnimation.Bounds
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.core.app.ActivityCompat

@SuppressLint("WrongViewCast")
class TestFonctionalities : AppCompatActivity() {

    private lateinit var number_call : EditText
    private lateinit var number_sms : EditText
    private lateinit var message : EditText
    private lateinit var call_btn : Button
    private lateinit var sms_btn : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_test_fonctionalities)


        number_call = findViewById(R.id.number_call)
        number_sms = findViewById(R.id.number_sms)
        message = findViewById(R.id.message)
        call_btn = findViewById(R.id.appeler)
        sms_btn = findViewById(R.id.envoyer_sms)

        checkAllPermissions()

        call_btn.setOnClickListener {
            val phoneNumber = number_call.text.toString()

            if(phoneNumber.isNotEmpty()) {
                val callIntent = Intent(Intent.ACTION_CALL)
                callIntent.data = Uri.parse("tel:$phoneNumber")
                startActivity(callIntent)
            }
            number_call.setText("")

        }

        sms_btn.setOnClickListener {
            val phoneNumber = number_sms.text.toString()
            val message_text = message.text.toString()

            if(phoneNumber.isNotEmpty()) {
                var sms = SmsManager.getDefault()
                sms.sendTextMessage(phoneNumber, null, message_text, null, null)
            }
            else {
                print("Entrer un numéro de téléphone valide !")
            }
            number_sms.setText("")
            message.setText("")
            Toast.makeText(this, "Message envoyé.", Toast.LENGTH_SHORT).show()
        }
    }

    private fun checkAllPermissions() {
        if(ActivityCompat.checkSelfPermission(this, Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED ||
            ActivityCompat.checkSelfPermission(this, Manifest.permission.READ_PHONE_STATE) != PackageManager.PERMISSION_GRANTED ||
            ActivityCompat.checkSelfPermission(this, Manifest.permission.READ_CALL_LOG) != PackageManager.PERMISSION_GRANTED ||
            ActivityCompat.checkSelfPermission(this, Manifest.permission.SEND_SMS) != PackageManager.PERMISSION_GRANTED ||
            ActivityCompat.checkSelfPermission(this, Manifest.permission.RECEIVE_SMS) != PackageManager.PERMISSION_GRANTED ) {

            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.CALL_PHONE,
                                                                    Manifest.permission.SEND_SMS,
                                                                    Manifest.permission.RECEIVE_SMS,
                                                                    Manifest.permission.READ_PHONE_STATE,
                                                                    Manifest.permission.READ_CALL_LOG), 101)
        }
    }

}