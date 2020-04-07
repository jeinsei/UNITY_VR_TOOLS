using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class VRReticleParameter : MonoBehaviour
{
    public Camera raycastCamera; // Camera de reference pour le raycast
    public Image mainTarget; // icone du pointer
    public Sprite hitOff; // changement d'état hit on
    public Sprite hitOn; // changement d'état hit off
    public Sprite hitLoad; // changement d'état durant la teleportation
    public Sprite hitButton;
    public float waitingTime; // temps d'attente du timer durant le chargement de l'image
    public float gvrTimer; // Timer de l'icone
    public bool gvrStatuts; // Boolean du statut du chargement
                  

    private void FixedUpdate()
    {
        RaycastHit hit;

        if (Physics.Raycast(raycastCamera.transform.position, raycastCamera.transform.TransformDirection(Vector3.forward), out hit, Mathf.Infinity))
        {
            Debug.DrawRay(raycastCamera.transform.position, raycastCamera.transform.TransformDirection(Vector3.forward) * hit.distance, Color.yellow);
            Debug.Log("Did Hit");
            mainTarget.GetComponent<Image>().sprite = hitOn;
           // mainTarget.GetComponent<Animator>().Play("hitOn");

        }
        else
        {
            Debug.DrawRay(raycastCamera.transform.position, raycastCamera.transform.TransformDirection(Vector3.forward) * 1000, Color.white);
            Debug.Log("Did not Hit");
            mainTarget.GetComponent<Image>().sprite = hitOff;
           // mainTarget.GetComponent<Animator>().Play("hitOff");
            mainTarget.fillAmount = 1;
        }

    }
}