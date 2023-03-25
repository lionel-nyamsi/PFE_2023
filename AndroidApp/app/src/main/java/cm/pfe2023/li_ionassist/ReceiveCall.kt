package cm.pfe2023.li_ionassist

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.provider.CallLog
import android.telephony.TelephonyManager
import android.widget.Toast

class ReceiveCall : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        var log = listOf<String>(CallLog.Calls._ID,
            CallLog.Calls.NUMBER,
            CallLog.Calls.TYPE,
            CallLog.Calls.DURATION,
            CallLog.Calls.DATA_USAGE)

        if(intent.getStringExtra(TelephonyManager.EXTRA_STATE).equals(TelephonyManager.EXTRA_STATE_RINGING)) {
            Toast.makeText(context, "Appel entrant...", Toast.LENGTH_SHORT).show()
        }
        if(intent.getStringExtra(TelephonyManager.EXTRA_STATE).equals(TelephonyManager.EXTRA_STATE_OFFHOOK)) {
            Toast.makeText(context, "Appel en cous...", Toast.LENGTH_SHORT).show()
        }
        if(intent.getStringExtra(TelephonyManager.EXTRA_STATE).equals(TelephonyManager.EXTRA_STATE_IDLE)) {
            Toast.makeText(context, "Appel terminé...", Toast.LENGTH_SHORT).show()
        }
    }
}