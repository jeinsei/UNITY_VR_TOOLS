using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Teleportation : MonoBehaviour
{
    public GameObject player;
    public ReticleParameter reticleParameter;
    public int distanceOfRay = 100;
    private RaycastHit hit;
    public float RaycastTime; // temps d'attente du timer durant le chargement de l'image
    public float RaycastTimer; // Timer de l'icone

    private void Start()
    {
        reticleParameter = GameObject.Find("ManagerScript").GetComponent<ReticleParameter>();
    }

    // Update is called once per frame
    void Update()
    {

        Ray ray = reticleParameter.raycastCamera.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0.5f));

        if (Physics.Raycast(ray, out hit, distanceOfRay))
        {
         
            if (hit.transform.CompareTag("Teleport"))
            {
                reticleParameter.mainTarget.GetComponent<Image>().sprite = reticleParameter.hitLoad;
                RaycastTimer += Time.deltaTime;
                reticleParameter.mainTarget.fillAmount = RaycastTimer / RaycastTime;
            }

            if (RaycastTimer > RaycastTime)
            {
                hit.transform.gameObject.GetComponent<TeleportItem>().TeleportPlayer();
                reticleParameter.mainTarget.fillAmount = 1;

            }

        }

        else
        {
          
            RaycastTimer = 0;
        }
    }


}
