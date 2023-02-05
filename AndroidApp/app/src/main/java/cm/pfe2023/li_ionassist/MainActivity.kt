package cm.pfe2023.li_ionassist

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import cm.pfe2023.li_ionassist.fragments.RegistrationFragment

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.registrer_page)

        // Injecter le bloc de register
        val transaction = supportFragmentManager.beginTransaction()
        transaction.replace(R.id.frament_container, RegistrationFragment())
        transaction.addToBackStack(null)
        transaction.commit()
    }
}