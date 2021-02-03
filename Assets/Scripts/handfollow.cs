using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Runtime.InteropServices;

public class handfollow : MonoBehaviour
{

    public GameObject left_hand;
    public GameObject right_hand;

    // Start is called before the first frame update
    void Start()
    {
        Screen.sleepTimeout = SleepTimeout.NeverSleep;
    }

    // Update is called once per frame
    void Update()
    {
        transform.position = right_hand.transform.position;
        Debug.Log("DATA SecondaryHandTrigger " + OVRInput.Get(OVRInput.Axis1D.SecondaryHandTrigger));
        Debug.Log("DATA SecondaryThumbstickButton " + OVRInput.GetDown(OVRInput.Button.SecondaryThumbstick));
        Debug.Log("DATA SecondaryThumbstick " + OVRInput.Get(OVRInput.Axis2D.SecondaryThumbstick).ToString("0.000"));
        Debug.Log("DATA ButtonTwo " + OVRInput.Get(OVRInput.Button.Two));
        Debug.Log("DATA ButtonOne " + OVRInput.Get(OVRInput.Button.One));
        Debug.Log("DATA SecondaryIndexTrigger " + OVRInput.Get(OVRInput.Axis1D.SecondaryIndexTrigger));
        Debug.Log("DATA RightCoords " + right_hand.transform.position.ToString("0.000"));
        Debug.Log("DATA LeftCoords " + left_hand.transform.position.ToString("0.000"));
        Debug.Log("DATA ActiveControllers " + OVRInput.GetConnectedControllers());
    }
}
