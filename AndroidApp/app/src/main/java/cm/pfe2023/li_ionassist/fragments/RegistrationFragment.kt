package cm.pfe2023.li_ionassist.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import cm.pfe2023.li_ionassist.IntermediateActivity
import cm.pfe2023.li_ionassist.MainActivity
import cm.pfe2023.li_ionassist.R

class RegistrationFragment() : Fragment() {
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
            return inflater?.inflate(R.layout.fragment_registration, container, false)
    }
}