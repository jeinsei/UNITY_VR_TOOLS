using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VRTeleportItem : MonoBehaviour
{

    public void TeleportPlayer()
    {
        var player = GameObject.Find("ManagerScript").GetComponent<VRTeleportation>().player;

        player.transform.position = new Vector3(transform.position.x, transform.position.y +1.5f, transform.position.z);

        Debug.Log("TeleportPlayer");
    }
}
