using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using UnityEngine.Events;

[RequireComponent(typeof(EventTrigger))]
public class VRGazeClickButton : MonoBehaviour
{
    public EventTrigger eventTrigger;
    public VRReticleParameter reticleParameter;
    public UnityEvent customOnClick;
    public bool activeBoolButtton = false;


    private void Awake()
    {
        reticleParameter = FindObjectOfType<VRReticleParameter>().GetComponent<VRReticleParameter>();
    }

    void Start()
    {
        eventTrigger = this.gameObject.GetComponent<EventTrigger>();

        EventTrigger.Entry entryEnter = new EventTrigger.Entry();
        EventTrigger.Entry entryExit = new EventTrigger.Entry();
    
        entryEnter.eventID = EventTriggerType.PointerEnter;
        entryEnter.callback.AddListener((data) => { OnPointerEnter((PointerEventData)data); });
        eventTrigger.triggers.Add(entryEnter);

        entryExit.eventID = EventTriggerType.PointerExit;
        entryExit.callback.AddListener((data) => { OnPointerExit((PointerEventData)data); });
        eventTrigger.triggers.Add(entryExit);


    }

    void Update()
    {
        // si statut true alors timer basé sur le temps, rempli le fillAmount de l'image
        if (activeBoolButtton == true)
        {
            reticleParameter.mainTarget.GetComponent<Image>().sprite = reticleParameter.hitButton;
            reticleParameter.gvrTimer += Time.deltaTime;
            reticleParameter.mainTarget.fillAmount = reticleParameter.gvrTimer / reticleParameter.waitingTime;

            if (reticleParameter.gvrTimer > reticleParameter.waitingTime)
            {
                customOnClick.Invoke();
            }
        }
    }

    public void OnPointerEnter(PointerEventData data)
    {
        Debug.Log("ENTER called.");

        activeBoolButtton = true;
    }

    public void OnPointerExit(PointerEventData data)
    {
        Debug.Log("EXIT called.");
 
        activeBoolButtton = false;
        reticleParameter.gvrTimer = 0f;
        reticleParameter.mainTarget.fillAmount = 1;
    }


}
