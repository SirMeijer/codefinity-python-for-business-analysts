import matplotlib.pyplot as plt

def plot_sales_performance(summary_dict):
    # Write your code here
    plt.bar(summary_dict.keys(), summary_dict.values())
    plt.xlabel("Product Names")
    plt.ylabel("Revenues")
    plt.title("Sales Performance")
    for i, value in enumerate(summary_dict.values()):
        plt.text(i, value + 200, f"{value}", ha='center', fontweight='bold')
    
summary_dict = {"Widget": 15000, "Gadget": 12000, "Doohickey": 9000}
plot_sales_performance(summary_dict)
