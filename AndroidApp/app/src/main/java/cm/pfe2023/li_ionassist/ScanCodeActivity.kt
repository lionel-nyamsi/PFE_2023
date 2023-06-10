package cm.pfe2023.li_ionassist

import android.Manifest
import android.bluetooth.BluetoothAdapter
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.CountDownTimer
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

private const val CAMERA_REQUEST_CODE = 101
private const val REQUEST_ENABLE_BT = 101
var ADRESSE_PC = ""

@Suppress("DEPRECATION")
class ScanCodeActivity : AppCompatActivity() {

    private lateinit var codeScanner: CodeScanner
    private var qrcode_text : String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_scan_code)

        setupPermissions()
        scanQRCode()
    }

    private fun setupPermissions() {
        val permission = ContextCompat.checkSelfPermission(this,
                            android.Manifest.permission.CAMERA)
        if(permission != PackageManager.PERMISSION_GRANTED) {
            askCameraPermission()
        }
    }

    private fun askCameraPermission() {
        ActivityCompat.requestPermissions(this,
            arrayOf(android.Manifest.permission.CAMERA),
            CAMERA_REQUEST_CODE)
    }

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {

        when(requestCode){
            CAMERA_REQUEST_CODE -> {
                if(grantResults.isEmpty() || grantResults[0] != PackageManager.PERMISSION_GRANTED) {
                    Toast.makeText(this, "Vous devez autoriser l'accès à la caméra pour établir la connexion avec la console.", Toast.LENGTH_LONG)
                }
                else {
                    Toast.makeText(this, "Connexion...", Toast.LENGTH_SHORT)
                }
            }
        }
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    }

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
                    ADRESSE_PC = qrcode_text
                    connect()
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

    private fun connect() {
        val bluetoothAdapter = BluetoothAdapter.getDefaultAdapter()
        if(bluetoothAdapter == null){
            Toast.makeText(this, "Bluetooth indisponible.", Toast.LENGTH_SHORT).show()
        }
        else {
            if(!bluetoothAdapter.isEnabled){
                val intent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
                if (ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_CONNECT
                    ) != PackageManager.PERMISSION_GRANTED) {
                    ActivityCompat.requestPermissions(this,
                        arrayOf(android.Manifest.permission.BLUETOOTH_CONNECT), REQUEST_ENABLE_BT)
                }
                startActivityForResult(intent, REQUEST_ENABLE_BT)
            }

            try {
                val console = bluetoothAdapter.getRemoteDevice(ADRESSE_PC)
                val uuid = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")
                val socket = console.createInsecureRfcommSocketToServiceRecord(uuid)

                socket.connect()
                nextPage()
            } catch (error: IOException) {
                Toast.makeText(this, "Une erreur est survenue lors de la connexion.", Toast.LENGTH_LONG).show()
            }
        }
    }

    private fun nextPage() {
        val connection_succesful_page = Intent(this, ConnectionSuccesfulActivity()::class.java)
        startActivity(connection_succesful_page)
    }

}