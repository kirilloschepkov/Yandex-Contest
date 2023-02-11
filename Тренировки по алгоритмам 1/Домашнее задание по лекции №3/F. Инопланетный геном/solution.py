def get_genes(genome: str) -> list:
    return [genome[i-1] + genome[i] for i in range(1, len(genome))]


def f(fst_genome: str, scd_genome: str) -> str:
    fst_genes = get_genes(fst_genome)
    scd_genes = set(get_genes(scd_genome))
    return str(len([gen for gen in fst_genes if gen in scd_genes]))


print(f(input(), input()))
