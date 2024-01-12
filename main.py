from utils import (
    get_random_data,
    generate_half_sorted_list,
    get_fastest_sort_alg,
    determine_overal_champion,
)

EXECUTION_QTY = 100

# Prepared different test data
random_list_small_size = get_random_data(0, 1000, 1000)
random_list_mid_size = get_random_data(0, 1000, 500000)
random_list_large_size = get_random_data(0, 1000, 10000000)

half_sorted_small_size = generate_half_sorted_list(1000)
half_sorted_mid_size = generate_half_sorted_list(500000)
half_sorted_large_size = generate_half_sorted_list(10000000)

# Small list tests
small_size_list_champion = get_fastest_sort_alg(random_list_small_size, "small size")

# Middle size list tests
mid_size_list_champion = get_fastest_sort_alg(random_list_small_size, "middle size")

# Large size list tests
large_size_list_champion = get_fastest_sort_alg(random_list_small_size, "large size")

# Small list tests
small_half_sorted_size_list_champion = get_fastest_sort_alg(
    random_list_small_size, "small half sorted size"
)

# Middle size list tests
mid_half_sorted_size_list_champion = get_fastest_sort_alg(
    random_list_small_size, "middle half sorted size"
)

# Large size list tests
large_half_sorted_size_list_champion = get_fastest_sort_alg(
    random_list_small_size, "large half sorted size"
)

overal_test_champion = determine_overal_champion(
    [
        small_size_list_champion,
        mid_size_list_champion,
        large_size_list_champion,
        small_half_sorted_size_list_champion,
        mid_half_sorted_size_list_champion,
        large_half_sorted_size_list_champion,
    ]
)

print("Conclusion: ")
print(f"The fastest sorting algorithm based on all tests is: {overal_test_champion}")
