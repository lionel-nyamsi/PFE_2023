package cm.pfe2023.li_ionassist

import android.Manifest
import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.bluetooth.BluetoothSocket
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.core.app.ActivityCompat
import androidx.core.app.ActivityCompat.startActivityForResult
import java.io.IOException
import java.util.*

private const val BT_REQUEST_CODE = 1

class BluetoothClient(private val activity: android.app.Activity,
                      private val context: android.content.Context) {

    private val uuid: UUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB")
    private val adapter: BluetoothAdapter = BluetoothAdapter.getDefaultAdapter()
    private lateinit var socket: BluetoothSocket
    private lateinit var devicesList: ArrayAdapter<BluetoothDevice>

    private var state:Boolean = false


    fun getNearbyDevices(): ArrayAdapter<BluetoothDevice> {
        lateinit var nearbyDevices: ArrayAdapter<BluetoothDevice>

        if(adapter == null){
            Toast.makeText(context, "Bluetooth indisponible.", Toast.LENGTH_SHORT).show()
        }
        else {
            if (!adapter.isEnabled) {
                BluetoothAdapter.ACTION_REQUEST_ENABLE
                if (ActivityCompat.checkSelfPermission(context, Manifest.permission.BLUETOOTH_CONNECT
                    ) != PackageManager.PERMISSION_GRANTED) {
                    ActivityCompat.requestPermissions(
                        activity, arrayOf(Manifest.permission.BLUETOOTH_CONNECT),
                        BT_REQUEST_CODE)
                }
            }
            adapter.startDiscovery()

            val receiver = object: BroadcastReceiver() {
                override fun onReceive(context: Context?, intent: Intent?) {
                    val action = intent?.action

                    if (BluetoothDevice.ACTION_FOUND == action) {
                        val device = intent.getParcelableExtra<BluetoothDevice>(BluetoothDevice.EXTRA_DEVICE)
                        nearbyDevices.add(device)
                    }
                }
            }
        }

        return nearbyDevices
    }


    fun connect(serverAddress: String) {

        devicesList = getNearbyDevices()

        if (devicesList.isEmpty) {
            Toast.makeText(context, "Aucun périphérique Bluetooth détecté!", Toast.LENGTH_SHORT).show()
            this.connect(serverAddress)
        }
        else {
            for (i in 0 until devicesList.count) {
                val device = devicesList.getItem(i)
                if (device != null) {
                    if (device.address.toString() == serverAddress) {
                        try {
                            if (ActivityCompat.checkSelfPermission(context,
                                    Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
                                ActivityCompat.requestPermissions(activity, arrayOf(Manifest.permission.BLUETOOTH_CONNECT),
                                    BT_REQUEST_CODE)
                            }
                            socket = device.createRfcommSocketToServiceRecord(uuid)
                            adapter.cancelDiscovery()
                            socket.connect()
                            state = true
                            Toast.makeText(context, "Connexion établie.", Toast.LENGTH_SHORT).show()
                        } catch (e: IOException) {
                            Toast.makeText(context, "Une erreur est survenue.", Toast.LENGTH_SHORT).show()
                            this.disconnect()
                        }

                        break
                    }
                }
            }

        }
    }

    fun disconnect() {
        try {
            socket.close()
        }
        catch (e: IOException) {
            Toast.makeText(context, "Impossible de fermer le socket : ${e.message}.", Toast.LENGTH_SHORT).show()
        }
    }

    fun isConnected(): Boolean {
        if (state == true) return true
        else return false
    }
}