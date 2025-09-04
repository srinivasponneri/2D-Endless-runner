using UnityEngine;

public class ObstacleSpawner : MonoBehaviour
{
    public GameObject obstaclePrefab;
    public float spawnInterval = 2f;
    public float obstacleY = -1f;

    void Start()
    {
        InvokeRepeating("SpawnObstacle", 1f, spawnInterval);
    }

    void SpawnObstacle()
    {
        float xPos = transform.position.x;
        Vector2 spawnPos = new Vector2(xPos, obstacleY);
        Instantiate(obstaclePrefab, spawnPos, Quaternion.identity);
    }
}
