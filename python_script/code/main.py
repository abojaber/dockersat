import matplotlib.pyplot as plt
import numpy as np

# Benchmark results for Redis and KeyDB
rounds = ["Round 4", "Round 5", "Round 6"]

# Throughput (Ops/sec)
redis_ops = [99882.41, 99839.96, 99894.13]
keydb_ops = [99874.45, 99912.38, 99825.28]

# Average Latency (ms)
redis_avg_latency = [4.79, 5.79, 5.11]
keydb_avg_latency = [2.66, 3.23, 3.33]

# p50 Latency (ms)
redis_p50_latency = [5.02, 6.24, 5.50]
keydb_p50_latency = [2.27, 2.88, 2.94]

# Create subplots
fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Plot 1: Throughput (Ops/sec)
axes[0].plot(rounds, redis_ops, label="Redis", marker='o', color='blue')
axes[0].plot(rounds, keydb_ops, label="KeyDB", marker='o', color='green')
axes[0].set_title("Throughput (Ops/sec)")
axes[0].set_ylabel("Operations per Second")
axes[0].legend()
axes[0].grid(True)

# Plot 2: Average Latency (ms)
axes[1].plot(rounds, redis_avg_latency, label="Redis", marker='o', color='blue')
axes[1].plot(rounds, keydb_avg_latency, label="KeyDB", marker='o', color='green')
axes[1].set_title("Average Latency (ms)")
axes[1].set_ylabel("Latency (ms)")
axes[1].legend()
axes[1].grid(True)

# Plot 3: p50 Latency (ms)
axes[2].plot(rounds, redis_p50_latency, label="Redis", marker='o', color='blue')
axes[2].plot(rounds, keydb_p50_latency, label="KeyDB", marker='o', color='green')
axes[2].set_title("p50 Latency (ms)")
axes[2].set_xlabel("Rounds")
axes[2].set_ylabel("Latency (ms)")
axes[2].legend()
axes[2].grid(True)

# Adjust layout and save/show the plot
plt.tight_layout()
plt.savefig("benchmark_results.png")  # Save the graph as an image file
plt.show()  # Display the graph
