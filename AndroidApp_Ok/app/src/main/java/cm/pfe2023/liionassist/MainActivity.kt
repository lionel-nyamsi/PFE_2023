package cm.pfe2023.liionassist

import android.bluetooth.*
import android.bluetooth.le.ScanCallback
import android.bluetooth.le.ScanResult
import android.bluetooth.le.ScanSettings
import android.content.Context
import android.content.Intent
import android.os.*
import androidx.appcompat.app.AppCompatActivity
import android.widget.Toast
import java.util.*

private const val BT_REQUEST_CODE = 1

class MainActivity() : AppCompatActivity(){

    companion object {
        private val SERVICE_UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")
        private const val SERVER_ADDRESS = "88:83:5d:fd:7a:af"
        private const val SCAN_PERIOD_MS = 10000
    }

    private lateinit var bluetoothManager : BluetoothManager
    private lateinit var bluetoothAdapter : BluetoothAdapter
    private var bluetoothGatt: BluetoothGatt? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        bluetoothManager = getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
        bluetoothAdapter = bluetoothManager.adapter

        connectToServer()
    }

    private fun connectToServer() {
        if(!bluetoothAdapter.isEnabled) {
            Toast.makeText(this, "Le bluetooth de votre téléphone sera activé. Ne l'éteignez pas !", Toast.LENGTH_SHORT).show()
            val btEnableIntent = Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE)
            startActivityForResult(btEnableIntent, BT_REQUEST_CODE)
        }

        val gattCallback = object: BluetoothGattCallback() {
            override fun onConnectionStateChange(gatt: BluetoothGatt?, status: Int, newState: Int) {
                super.onConnectionStateChange(gatt, status, newState)

                if (newState == BluetoothProfile.STATE_CONNECTED) {
                    gatt?.discoverServices()
                }
                else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
                    Toast.makeText(this@MainActivity, "Connexion perdue. Tentative de reconnexion...", Toast.LENGTH_SHORT).show()
                }
            }

            override fun onServicesDiscovered(gatt: BluetoothGatt?, status: Int) {
                super.onServicesDiscovered(gatt, status)

                if (status == BluetoothGatt.GATT_SUCCESS) {
                    val service = gatt?.getService(SERVICE_UUID)
                    if (service == null) {
                        Toast.makeText(this@MainActivity, "Service Bluetooth pas trouvé.", Toast.LENGTH_SHORT).show()
                        gatt?.disconnect()
                    }
                }
                else {
                    Toast.makeText(this@MainActivity, "Erreur lors de la découverte des services Bluetooth.", Toast.LENGTH_SHORT).show()
                    gatt?.disconnect()
                }
            }
        }

        val scanCallback = object: ScanCallback() {
            override fun onScanResult(callbackType: Int, result: ScanResult?) {
                super.onScanResult(callbackType, result)

                if (result?.device?.address == SERVER_ADDRESS) {
                    bluetoothAdapter.bluetoothLeScanner.stopScan(this)

                    bluetoothGatt = result.device.connectGatt(this@MainActivity, true, gattCallback)
                }
            }
        }

        val scanSettings = ScanSettings.Builder().setScanMode(ScanSettings.SCAN_MODE_LOW_POWER).build()
        bluetoothAdapter.bluetoothLeScanner.startScan(null, scanSettings, scanCallback)

        Handler(Looper.getMainLooper()).postDelayed({
            bluetoothAdapter.bluetoothLeScanner.stopScan(scanCallback)
            if(bluetoothGatt == null) {
                Toast.makeText(this, "La console n'a pas été détectée. Veuillez réessyer !", Toast.LENGTH_SHORT).show()
            }

        }, SCAN_PERIOD_MS.toLong())

    }

    override fun onDestroy() {
        super.onDestroy()

        bluetoothGatt?.disconnect()
        bluetoothGatt?.close()
    }


}