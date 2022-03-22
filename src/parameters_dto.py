class ParametersDto:
    range_a = None
    range_b = None
    population_amount = None
    number_of_bits = None
    epochs_amount = None
    best_and_tournament_chromosome_amount = None
    elite_stategy_amount = None
    cross_probability = None
    mutation_probability = None
    inversion_probability = None
    selection_method = None
    cross_method = None
    mutation_method = None

    def __init__(self, range_a,
                 range_b,
                 population_amount,
                 number_of_bits,
                 epochs_amount,
                 best_and_tournament_chromosome_amount,
                 elite_stategy_amount,
                 cross_probability,
                 mutation_probability,
                 inversion_probability,
                 selection_method,
                 cross_method,
                 mutation_method,) -> None:
        self.range_a = range_a
        self.range_b = range_b
        self.population_amount = population_amount
        self.number_of_bits = number_of_bits
        self.epochs_amount = epochs_amount
        self.best_and_tournament_chromosome_amount = best_and_tournament_chromosome_amount
        self.elite_stategy_amount = elite_stategy_amount
        self.cross_probability = cross_probability
        self.mutation_probability = mutation_probability
        self.inversion_probability = inversion_probability
        self.selection_method = selection_method
        self.cross_method = cross_method
        self.mutation_method = mutation_method
        pass
