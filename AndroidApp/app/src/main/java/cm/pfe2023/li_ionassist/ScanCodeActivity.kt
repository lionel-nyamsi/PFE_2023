package cm.pfe2023.li_ionassist

import android.Manifest
import android.annotation.SuppressLint
import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.bluetooth.BluetoothSocket
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.CountDownTimer
import android.provider.ContactsContract
import android.util.Log
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.budiyev.android.codescanner.AutoFocusMode
import com.budiyev.android.codescanner.CodeScanner
import com.budiyev.android.codescanner.CodeScannerView
import com.budiyev.android.codescanner.DecodeCallback
import com.budiyev.android.codescanner.ErrorCallback
import com.budiyev.android.codescanner.ScanMode
import java.io.IOException
import java.util.*
import kotlin.collections.ArrayList

private const val CAMERA_REQUEST_CODE = 101
private const val REQUEST_ENABLE_BT = 101
private const val CONTACT_REQUEST_CODE = 100

var contactsList : MutableList<String> = mutableListOf()

var ADRESSE_CONSOLE = ""

@Suppress("DEPRECATION")
class ScanCodeActivity : AppCompatActivity() {

    private lateinit var codeScanner: CodeScanner
    private var qrcode_text : String = ""

    @RequiresApi(Build.VERSION_CODES.S)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_scan_code)

        setupPermissions()
        scanQRCode()
    }

    private fun setupPermissions() {
        val permissionCamera = ContextCompat.checkSelfPermission(this,
                            android.Manifest.permission.CAMERA)
        val accesContactPermission = ContextCompat.checkSelfPermission(this,
                            android.Manifest.permission.READ_CONTACTS)

        if(permissionCamera != PackageManager.PERMISSION_GRANTED) {
            askCameraPermission()
        }
        if(accesContactPermission != PackageManager.PERMISSION_GRANTED) {
            askContactPermission()
        }
    }

    private fun askCameraPermission() {
        ActivityCompat.requestPermissions(this,
            arrayOf(android.Manifest.permission.CAMERA),
            CAMERA_REQUEST_CODE)
    }

    private fun askContactPermission() {
        ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.READ_CONTACTS,
                                                                android.Manifest.permission.WRITE_CONTACTS),
                                                        CONTACT_REQUEST_CODE)
    }

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {

        when(requestCode){
            CAMERA_REQUEST_CODE -> {
                if(grantResults.isEmpty() || grantResults[0] != PackageManager.PERMISSION_GRANTED) {
                    Toast.makeText(this, "Vous devez autoriser l'accès à la caméra pour établir la connexion avec la console.", Toast.LENGTH_LONG).show()
                }
                else {
                    Toast.makeText(this, "Connexion...", Toast.LENGTH_SHORT).show()
                }
            }
        }
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    }

    @RequiresApi(Build.VERSION_CODES.S)
    private fun scanQRCode() {
        val scanner_view = findViewById<CodeScannerView>(R.id.scanner_data)
        codeScanner = CodeScanner(this, scanner_view)

        codeScanner.apply {
            camera = CodeScanner.CAMERA_BACK
            formats = CodeScanner.ALL_FORMATS

            autoFocusMode = AutoFocusMode.SAFE
            scanMode = ScanMode.CONTINUOUS
            isAutoFocusEnabled = true
            isFlashEnabled = false

            decodeCallback = DecodeCallback {
                runOnUiThread {
                    qrcode_text = it.text
                    ADRESSE_CONSOLE = qrcode_text
                    if(connect())
                        nextPage()
                    //else
                        //Toast.makeText(this, "La tentative de connexion a échouée. Veuillez réessayer!", Toast.LENGTH_SHORT).show()

                }
            }

            errorCallback = ErrorCallback {
                runOnUiThread {
                    Log.e("Main", "Erreur d'initialisation de la caméra : ${it.message}")
                }
            }
        }

        scanner_view.setOnClickListener{
            codeScanner.startPreview()              // Car, sacnMode = CONTINOUS
        }
    }

    override fun onResume() {
        super.onResume()
        codeScanner.startPreview()
    }

    override fun onPause() {
        codeScanner.releaseResources()
        super.onPause()
    }


    private fun connect(): Boolean {
        val bluetoothClient = BluetoothClient(this, this)
        bluetoothClient.connect("88:83:5d:fd:7a:af")

        return bluetoothClient.isConnected()
    }

    private fun nextPage() {
        setContentView(R.layout.fragment_connection_succesful)
    }

    /*@SuppressLint("Range")
    @RequiresApi(Build.VERSION_CODES.O)
    private fun readContact() {
        val contacts = contentResolver.query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, null, null, null)
        if (contacts != null) {
            while (contacts.moveToNext()) {
                val name = contacts.getString(contacts.getColumnIndex(ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME))
                val number = contacts.getString(contacts.getColumnIndex(ContactsContract.CommonDataKinds.Phone.NUMBER))

                contactsList.add(name)
            }
        }
    }*/

}

