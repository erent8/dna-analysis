# import tkinter as tk
# from tkinter import ttk

# def calculate_gc_content(sequence):
#     gc_count = sequence.upper().count('G') + sequence.upper().count('C')
#     gc_content = (gc_count / len(sequence)) * 100
#     return gc_content

# def calculate_at_content(sequence):
#     at_count = sequence.upper().count('A') + sequence.upper().count('T')
#     at_content = (at_count / len(sequence)) * 100
#     return at_content

# def calculate_purine_pyrimidine_ratio(sequence):
#     purine_count = sequence.upper().count('A') + sequence.upper().count('G')
#     pyrimidine_count = sequence.upper().count('C') + sequence.upper().count('T')
#     ratio = purine_count / pyrimidine_count if pyrimidine_count != 0 else float('inf')
#     return ratio

# def calculate_tm(sequence, gc_factor=4.0, at_factor=2.0):
#     gc_count = sequence.upper().count('G') + sequence.upper().count('C')
#     at_count = len(sequence) - gc_count
#     tm = (gc_count * gc_factor) + (at_count * at_factor)
#     return tm

# def calculate_denaturation_temperature(sequence):
#     return calculate_tm(sequence) + 5

# def calculate_extension_temperature(sequence):
#     return calculate_tm(sequence) - 5

# def analyze_sequence():
#     sequence = sequence_entry.get()

#     if sequence:
#         gc_content = calculate_gc_content(sequence)
#         at_content = calculate_at_content(sequence)
#         purine_pyrimidine_ratio = calculate_purine_pyrimidine_ratio(sequence)
#         optimal_tm = calculate_tm(sequence)
#         denaturation_temp = calculate_denaturation_temperature(sequence)
#         extension_temp = calculate_extension_temperature(sequence)
        
        
#         result_text.set(f"GC İçeriği: {gc_content:.2f}%\n"
#                         f"AT İçeriği: {at_content:.2f}%\n"
#                         f"Purin-Pirimidin Oranı: {purine_pyrimidine_ratio:.2f}\n"
#                         f"Optimum Bağlanma Sıcaklığı (Tm): {optimal_tm:.2f}°C\n"
#                         f"Denatürasyon Sıcaklığı (Td): {denaturation_temp:.2f}°C\n"
#                         f"Uzama Sıcaklığı (Te): {extension_temp:.2f}°C")
#     else:
#         result_text.set("Lütfen bir DNA dizisi girin!")

# # Tkinter penceresi oluştur
# root = tk.Tk()
# root.title("DNA ANALİZİ UYGULAMASI")

# # Stil tema
# style = ttk.Style()
# style.theme_use("clam")  # farklı temaları deneyebilirsiniz

# # Ana çerçeve
# main_frame = ttk.Frame(root, padding="20")
# main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# # Başlık etiketi
# title_label = ttk.Label(main_frame, text="DNA Analiz Programı", font=("Helvetica", 16))
# title_label.grid(column=0, row=0, columnspan=2, pady=10)

# # Giriş etiketi ve giriş alanı
# sequence_label = ttk.Label(main_frame, text="DNA Dizisini Giriniz:")
# sequence_label.grid(column=0, row=1, sticky=tk.W, pady=5)
# sequence_entry = ttk.Entry(main_frame, width=50)
# sequence_entry.grid(column=1, row=1, pady=5)

# # Analiz butonu
# analyze_button = ttk.Button(main_frame, text="Diziyi Analiz Et", command=analyze_sequence)
# analyze_button.grid(column=0, row=2, columnspan=2, pady=10)

# # Sonuç etiketi
# result_text = tk.StringVar()
# result_label = ttk.Label(main_frame, textvariable=result_text)
# result_label.grid(column=0, row=3, columnspan=2, pady=10)

# # Pencereyi başlat
# root.mainloop()




import tkinter as tk
from tkinter import ttk

def calculate_gc_content(sequence):
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    gc_content = (gc_count / len(sequence)) * 100
    return gc_content

def calculate_at_content(sequence):
    at_count = sequence.upper().count('A') + sequence.upper().count('T')
    at_content = (at_count / len(sequence)) * 100
    return at_content

def calculate_purine_pyrimidine_ratio(sequence):
    purine_count = sequence.upper().count('A') + sequence.upper().count('G')
    pyrimidine_count = sequence.upper().count('C') + sequence.upper().count('T')
    ratio = purine_count / pyrimidine_count if pyrimidine_count != 0 else float('inf')
    return ratio

def calculate_tm(sequence, gc_factor=4.0, at_factor=2.0):
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    at_count = len(sequence) - gc_count
    tm = (gc_count * gc_factor) + (at_count * at_factor)
    return tm

def calculate_denaturation_temperature(sequence):
    return calculate_tm(sequence) + 5

def calculate_extension_temperature(sequence):
    return calculate_tm(sequence) - 5

def is_valid_sequence(sequence):
    valid_bases = set("ACGT")
    return all(base.upper() in valid_bases for base in sequence)

def analyze_sequence():
    sequence = sequence_entry.get()

    if sequence:
        gc_content = calculate_gc_content(sequence)
        at_content = calculate_at_content(sequence)
        purine_pyrimidine_ratio = calculate_purine_pyrimidine_ratio(sequence)
        optimal_tm = calculate_tm(sequence)
        denaturation_temp = calculate_denaturation_temperature(sequence)
        extension_temp = calculate_extension_temperature(sequence)

        result_text.set(f"GC İçeriği: {gc_content:.2f}%\n"
                        f"AT İçeriği: {at_content:.2f}%\n"
                        f"Purin-Pirimidin Oranı: {purine_pyrimidine_ratio:.2f}\n"
                        f"Optimum Bağlanma Sıcaklığı (Tm): {optimal_tm:.2f}°C\n"
                        f"Denatürasyon Sıcaklığı (Td): {denaturation_temp:.2f}°C\n"
                        f"Uzama Sıcaklığı (Te): {extension_temp:.2f}°C")

        update_thermometer(denaturation_temp, extension_temp)
    else:
        result_text.set("Lütfen bir DNA dizisi girin!")

def update_thermometer(denaturation_temp, extension_temp):
    denaturation_scale.set(denaturation_temp)
    extension_scale.set(extension_temp)

    denaturation_canvas.delete("all")
    denaturation_height = (denaturation_temp / 100) * 100
    denaturation_canvas.create_rectangle(0, 100 - denaturation_height, 20, 100, fill="red")

    extension_canvas.delete("all")
    extension_height = (extension_temp / 100) * 100
    extension_canvas.create_rectangle(0, 100 - extension_height, 20, 100, fill="blue")

# Tkinter penceresi oluştur
root = tk.Tk()
root.title("DNA ANALİZİ UYGULAMASI")

# Stil tema
style = ttk.Style()
style.theme_use("clam")  # farklı temaları deneyebilirsiniz

# Ana çerçeve
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Başlık etiketi
title_label = ttk.Label(main_frame, text="DNA Analiz Programı", font=("Helvetica", 16))
title_label.grid(column=0, row=0, columnspan=2, pady=10)

# Giriş etiketi ve giriş alanı
sequence_label = ttk.Label(main_frame, text="DNA Dizisini Giriniz:")
sequence_label.grid(column=0, row=1, sticky=tk.W, pady=5)
sequence_entry = ttk.Entry(main_frame, width=50)
sequence_entry.grid(column=1, row=1, pady=5)

# Analiz butonu
analyze_button = ttk.Button(main_frame, text="Diziyi Analiz Et", command=analyze_sequence)
analyze_button.grid(column=0, row=2, columnspan=2, pady=10)

# Sonuç etiketi
result_text = tk.StringVar()
result_label = ttk.Label(main_frame, textvariable=result_text)
result_label.grid(column=0, row=3, columnspan=2, pady=10)

# Termometre gösterimi
thermometer_frame = ttk.Frame(main_frame)
thermometer_frame.grid(column=0, row=4, columnspan=2, pady=10)

denaturation_label = ttk.Label(thermometer_frame, text="Denatürasyon Sıcaklığı")
denaturation_label.grid(column=0, row=0, padx=10)

denaturation_scale = ttk.Scale(thermometer_frame, from_=0, to=100, orient="horizontal", length=200)
denaturation_scale.grid(column=1, row=0, padx=10)

denaturation_canvas = tk.Canvas(thermometer_frame, width=20, height=100, background="lightblue")
denaturation_canvas.grid(column=2, row=0, padx=10)

extension_label = ttk.Label(thermometer_frame, text="Uzama Sıcaklığı")
extension_label.grid(column=3, row=0, padx=10)

extension_scale = ttk.Scale(thermometer_frame, from_=0, to=100, orient="horizontal", length=200)
extension_scale.grid(column=4, row=0, padx=10)

extension_canvas = tk.Canvas(thermometer_frame, width=20, height=100, background="lightblue")
extension_canvas.grid(column=5, row=0, padx=10)

# Pencereyi başlat
root.mainloop()
