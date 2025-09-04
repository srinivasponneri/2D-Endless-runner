using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float runSpeed = 5f;
    public float jumpForce = 10f;
    private Rigidbody2D rb;
    private bool isGrounded = true;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    void Update()
    {
        // Auto-run
        rb.velocity = new Vector2(runSpeed, rb.velocity.y);

        // Jump
        if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
        {
            rb.velocity = new Vector2(rb.velocity.x, jumpForce);
            isGrounded = false;
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.collider.CompareTag("Ground"))
        {
            isGrounded = true;
        }
        else if (collision.collider.CompareTag("Obstacle"))
        {
            Debug.Log("Game Over!");
            Time.timeScale = 0; // Stop game
        }
    }
}
