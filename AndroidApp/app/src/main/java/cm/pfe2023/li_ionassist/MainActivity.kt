package cm.pfe2023.li_ionassist

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import cm.pfe2023.li_ionassist.fragments.ConnectionFragment
import cm.pfe2023.li_ionassist.fragments.RegistrationFragment
import cm.pfe2023.li_ionassist.fragments.ScanCodeFragment
import cm.pfe2023.li_ionassist.fragments.WelcomeFragment

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* Injecter le fragment de register
        val transaction = supportFragmentManager.beginTransaction()
        transaction.replace(R.id.fragment_container, RegistrationFragment())
        transaction.addToBackStack(null)
        transaction.commit()*/
    }
}