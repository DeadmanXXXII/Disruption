#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <unistd.h>

void *memory_corruption(void *arg) {
    // Create a buffer and intentionally overflow it
    char buffer[100];
    for (int i = 0; i < 1000000000; i++) {
        memset(buffer, 'A', sizeof(buffer) + 500);  // Buffer overflow!
    }
    return NULL;
}

void *cpu_stress(void *arg) {
    // Infinite loop to stress CPU
    while (1) {}
    return NULL;
}

void fork_bomb() {
    while (1) {
        if (fork() == 0) {
            exit(0);  // Child exits immediately, but the fork storm continues
        }
    }
}

int main() {
    pthread_t threads[10];

    // Start memory corruption threads
    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, memory_corruption, NULL);
    }

    // Start CPU stress threads
    for (int i = 5; i < 10; i++) {
        pthread_create(&threads[i], NULL, cpu_stress, NULL);
    }

    // Trigger fork bomb (fork storm to overwhelm process table)
    fork_bomb();

    // Join threads (though they'll never finish)
    for (int i = 0; i < 10; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}