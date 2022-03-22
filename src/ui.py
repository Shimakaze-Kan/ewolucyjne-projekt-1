from tkinter import *
from tkinter.ttk import Combobox

from calculations_manager import CalculationsManager
from parameters_dto import ParametersDto


class UI:
    window = Tk()
    input_range_a = Entry(window)
    input_range_b = Entry(window)
    input_population_amount = Entry(window)
    input_number_of_bits = Entry(window)
    input_epochs_amount = Entry(window)
    input_best_and_tournament_chromosome_amount = Entry(window)
    input_elite_stategy_amount = Entry(window)
    input_cross_probability = Entry(window)
    input_mutation_probability = Entry(window)
    input_inversion_probability = Entry(window)
    selection_methods = ("Best", "Roulette", "Tournament")
    cb_selection_method = Combobox(window, values=selection_methods)
    cross_methods = ("one_point", "two_points", "three_points", "homo")
    cb_cross_method = Combobox(window, values=cross_methods)
    mutation_methods = ("one_point", "two_points")
    cb_mutation_method = Combobox(window, values=mutation_methods)
    btn_start = None

    def __init__(self) -> None:

        self.btn_start = Button(self.window, text="Start",
                                command=self.start_click, fg='blue')
        self.show_controls()
        self.window.title("Metody ewolucyjne projekt nr 1")
        self.window.geometry("400x500+10+10")
        self.window.mainloop()
        pass

    def show_controls(self) -> None:
        self.show_labels()

        self.input_range_a.place(x=10, y=32)
        self.input_range_b.place(x=10, y=92)
        self.input_population_amount.place(x=10, y=152)
        self.input_number_of_bits.place(x=10, y=212)
        self.input_epochs_amount.place(x=10, y=272)
        self.input_best_and_tournament_chromosome_amount.place(x=10, y=332)
        self.input_elite_stategy_amount.place(x=10, y=392)
        self.input_cross_probability.place(x=10, y=452)
        self.input_mutation_probability.place(x=190, y=32)
        self.input_inversion_probability.place(x=190, y=92)
        self.cb_selection_method.place(x=190, y=152)
        self.cb_cross_method.place(x=190, y=212)
        self.cb_mutation_method.place(x=190, y=272)
        self.btn_start.place(x=190, y=312)

    def show_labels(self) -> None:
        label_input_range_a = Label(self.window, text="Begin of range - a")
        label_input_range_b = Label(self.window, text="Begin of range - b")
        label_input_population_amount = Label(
            self.window, text="Population amount")
        label_input_number_of_bits = Label(self.window, text="Number of bits")
        label_input_epochs_amount = Label(self.window, text="Epochs amount")
        label_input_best_and_tournament_chromosome_amount = Label(
            self.window, text="Best and tournament\n chromosome amount")
        label_input_elite_stategy_amount = Label(
            self.window, text="Elite strategy amount")
        label_input_cross_probability = Label(
            self.window, text="Cross probability")
        label_input_mutation_probability = Label(
            self.window, text="Mutation probability")
        label_input_inversion_probability = Label(
            self.window, text="Inversion probability")
        label_cb_selection_method = Label(self.window, text="Selection method")
        label_cb_cross_method = Label(self.window, text="Cross method")
        label_cb_mutation_method = Label(self.window, text="Mutation method")

        label_input_range_a.place(x=10, y=10)
        label_input_range_b.place(x=10, y=70)
        label_input_population_amount.place(x=10, y=130)
        label_input_number_of_bits.place(x=10, y=190)
        label_input_epochs_amount.place(x=10, y=250)
        label_input_best_and_tournament_chromosome_amount.place(x=10, y=295)
        label_input_elite_stategy_amount.place(x=10, y=370)
        label_input_cross_probability.place(x=10, y=430)
        label_input_mutation_probability.place(x=190, y=10)
        label_input_inversion_probability.place(x=190, y=70)
        label_cb_selection_method.place(x=190, y=130)
        label_cb_cross_method.place(x=190, y=190)
        label_cb_mutation_method.place(x=190, y=250)

    def start_click(self) -> None:
        calculations_manager = CalculationsManager(self.get_params())
        calculations_manager.start()
        self.open_popup()

    def get_params(self) -> ParametersDto:
        return ParametersDto(self.input_range_a.get(),
                             self.input_range_b.get(),
                             self.input_population_amount.get(),
                             self.input_number_of_bits.get(),
                             self.input_epochs_amount.get(),
                             self.input_best_and_tournament_chromosome_amount.get(),
                             self.input_elite_stategy_amount.get(),
                             self.input_cross_probability.get(),
                             self.input_mutation_probability.get(),
                             self.input_inversion_probability.get(),
                             self.cb_selection_method.get(),
                             self.cb_cross_method.get(),
                             self.cb_mutation_method.get(),)

    def open_popup(self) -> None: # todo: remove 
        top = Toplevel(self.window)
        top.geometry("200x100")
        top.title("Calculations")
        Label(top, text="Done", font=('Mistral 18 bold')).place(x=10, y=10)
