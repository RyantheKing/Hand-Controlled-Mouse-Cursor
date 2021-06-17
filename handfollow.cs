using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Runtime.InteropServices;

public class handfollow : MonoBehaviour
{
    
    public GameObject left_hand;
    public GameObject right_hand;
    private bool rightHand = true;
    private string controller_type = OVRInput.GetConnectedControllers().ToString();

    // Start is called before the first frame update
    void Start()
    {
        Screen.sleepTimeout = SleepTimeout.NeverSleep;
    }

    // Update is called once per frame
    void Update()
    {
        //Physics.Raycast(right_hand.transform.position, -right_hand.transform.forward, Mathf.Infinity);
        controller_type = OVRInput.GetConnectedControllers().ToString();
        if (controller_type == "Touch") {
            Debug.Log("DATA SecondaryHandTrigger " + OVRInput.Get(OVRInput.Axis1D.SecondaryHandTrigger));
            Debug.Log("DATA SecondaryThumbstickButton " + OVRInput.GetDown(OVRInput.Button.SecondaryThumbstick));
            Debug.Log("DATA SecondaryThumbstick " + OVRInput.Get(OVRInput.Axis2D.SecondaryThumbstick).ToString("0.0000"));
            Debug.Log("DATA ButtonTwo " + OVRInput.Get(OVRInput.Button.Two));
            Debug.Log("DATA ButtonOne " + OVRInput.Get(OVRInput.Button.One));
            Debug.Log("DATA SecondaryIndexTrigger " + OVRInput.Get(OVRInput.Axis1D.SecondaryIndexTrigger));
            Debug.Log("DATA RightCoords " + OVRInput.GetLocalControllerPosition(OVRInput.Controller.RTouch).ToString("0.0000"));
            //Debug.Log("DATA RightPolCoords " + (-right_hand.transform.forward).ToString("0.0000"));
            //Debug.Log("DATA RightPolCoords " + right_hand.transform.eulerAngles.ToString("0.0000"));
            //Debug.Log("DATA LeftCoords " + left_hand.transform.position.ToString("0.0000"));
        } else if (controller_type == "RTouch") {
            Debug.Log("DATA SecondaryHandTrigger " + OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger));
            Debug.Log("DATA SecondaryThumbstickButton " + OVRInput.GetDown(OVRInput.Button.PrimaryThumbstick));
            Debug.Log("DATA SecondaryThumbstick " + OVRInput.Get(OVRInput.Axis2D.PrimaryThumbstick).ToString("0.0000"));
            Debug.Log("DATA ButtonTwo " + OVRInput.Get(OVRInput.Button.Two));
            Debug.Log("DATA ButtonOne " + OVRInput.Get(OVRInput.Button.One));
            Debug.Log("DATA SecondaryIndexTrigger " + OVRInput.Get(OVRInput.Axis1D.PrimaryIndexTrigger));
            Debug.Log("DATA RightCoords " + OVRInput.GetLocalControllerPosition(OVRInput.Controller.RTouch).ToString("0.0000"));
        } else if (controller_type == "LTouch") {
            //transform.position = left_hand.transform.position;
            Debug.Log("DATA SecondaryHandTrigger " + OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger));
            Debug.Log("DATA SecondaryThumbstickButton " + OVRInput.GetDown(OVRInput.Button.PrimaryThumbstick));
            Debug.Log("DATA SecondaryThumbstick " + OVRInput.Get(OVRInput.Axis2D.PrimaryThumbstick).ToString("0.0000"));
            Debug.Log("DATA ButtonTwo " + OVRInput.Get(OVRInput.Button.Two));
            Debug.Log("DATA ButtonOne " + OVRInput.Get(OVRInput.Button.One));
            Debug.Log("DATA SecondaryIndexTrigger " + OVRInput.Get(OVRInput.Axis1D.PrimaryIndexTrigger));
            Debug.Log("DATA RightCoords " + OVRInput.GetLocalControllerPosition(OVRInput.Controller.LTouch).ToString("0.0000"));
        } else if (controller_type == "Hands") {
            var right_hand_component = right_hand.GetComponent<OVRHand>();
            var left_hand_component = left_hand.GetComponent<OVRHand>();
            //Debug.Log("DATA Test "+left_hand_component.IsTracked+right_hand_component.IsTracked+left_hand_component.HandConfidence+right_hand_component.HandConfidence);
            if (left_hand_component.IsTracked) {
                if (right_hand_component.IsTracked) {
                    if ((left_hand_component.HandConfidence == OVRHand.TrackingConfidence.Low) && (right_hand_component.HandConfidence == OVRHand.TrackingConfidence.High)) {
                        Debug.Log("DATA RightCoords " + right_hand_component.PointerPose.localPosition.ToString("0.0000"));
                        rightHand = true;
                    } else {
                        Debug.Log("DATA RightCoords " + left_hand_component.PointerPose.localPosition.ToString("0.0000"));
                        rightHand = false;
                    }
                } else {
                    Debug.Log("DATA RightCoords " + left_hand_component.PointerPose.localPosition.ToString("0.0000"));
                    rightHand = false;
                }
            } else if (right_hand_component.IsTracked) {
                Debug.Log("DATA RightCoords " + right_hand_component.PointerPose.localPosition.ToString("0.0000"));
                rightHand = true;
            }
            // pinch test
            if (rightHand) {
                Debug.Log("DATA IndexPinch " + right_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Index));
            } else {
                Debug.Log("DATA IndexPinch " + left_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Index));
            }
            // right click
            if (rightHand) {
                Debug.Log("DATA MiddlePinch " + right_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Middle));
            } else {
                Debug.Log("DATA MiddlePinch " + left_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Middle));
            }
            if (rightHand) {
                Debug.Log("DATA RingPinch " + right_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Ring));
            } else {
                Debug.Log("DATA RingPinch " + left_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Ring));
            }
            // right click
            if (rightHand) {
                Debug.Log("DATA PinkyPinch " + right_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Pinky));
            } else {
                Debug.Log("DATA PinkyPinch " + left_hand_component.GetFingerIsPinching(OVRHand.HandFinger.Pinky));
            }
        }
    }
}
