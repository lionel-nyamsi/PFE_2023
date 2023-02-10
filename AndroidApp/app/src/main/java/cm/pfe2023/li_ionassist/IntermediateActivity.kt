package cm.pfe2023.li_ionassist

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import cm.pfe2023.li_ionassist.fragments.ConnectionFragment
import cm.pfe2023.li_ionassist.fragments.RegistrationFragment
import cm.pfe2023.li_ionassist.fragments.ScanCodeFragment

class IntermediateActivity() : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_intermediate)

        val transaction = supportFragmentManager.beginTransaction()
        transaction.replace(R.id.fragment_container, RegistrationFragment())
        transaction.addToBackStack(null)
        transaction.commit()

        /* Injection du contenu du fragment _fragmentContainer_
        when(_fragment)
        {
            R.layout.fragment_registration -> {
                loadFragment(RegistrationFragment())
            }
            R.layout.fragment_connection -> {
                loadFragment(ConnectionFragment())
            }
            R.layout.fragment_scan -> {
                loadFragment(ScanCodeFragment())
            }
            else -> {
                loadFragment(RegistrationFragment())
            }
        }*/
    }

    private fun loadFragment(frag: Fragment) {
        val transaction = supportFragmentManager.beginTransaction()
        transaction.replace(R.id.fragment_container, RegistrationFragment())
        transaction.addToBackStack(null)
        transaction.commit()
    }

}