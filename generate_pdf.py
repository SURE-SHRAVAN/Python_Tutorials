from fpdf import FPDF   
# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Add a title
pdf.cell(200, 10, txt="Short Answers for Chemistry Questions - Part 2", ln=True, align='C')

# Add the content with encoding corrections
content = [
    "1. a) Calculate the Bond Order of Oxygen Molecule (2M, CO1, L4)",
    "Using Molecular Orbital Theory, the bond order of the O2 molecule is calculated as:",
    "Bond Order = 1/2 (N_b - N_a) = 1/2 (10 - 6) = 2",
    "",
    "1. b) Significance of Ψ and Ψ² (2M, CO1, L3)",
    "Ψ (Psi): The wave function that describes the quantum state of a particle. It contains all the information about the system.",
    "Ψ² (Psi squared): Represents the probability density of finding a particle in a particular region of space. It is used to determine the likelihood of a particle's presence.",
    "",
    "1. c) Applications of Semiconductors (2M, CO2, L3)",
    "1. Used in the fabrication of electronic devices such as diodes, transistors, and integrated circuits (ICs).",
    "2. Employed in photovoltaic cells for solar energy conversion.",
    "",
    "1. d) What are Nanomaterials? (2M, CO2, L2)",
    "Nanomaterials are materials with structural components smaller than 100 nanometers. They exhibit unique properties due to their small size and large surface area.",
    "",
    "1. e) What is an Electrochemical Cell? (2M, CO3, L1)",
    "An electrochemical cell is a device that generates electrical energy from chemical reactions or facilitates chemical reactions through the introduction of electrical energy.",
    "",
    "1. f) Reactions in Hydrogen-Oxygen Fuel Cell (2M, CO3, L4)",
    "1. Anode reaction: H2 -> 2H+ + 2e-",
    "2. Cathode reaction: 1/2 O2 + 2H+ + 2e- -> H2O",
    "",
    "1. g) Preparation, Properties, and Applications of Polyvinyl Chloride (2M, CO4, L3)",
    "Preparation: Polymerization of vinyl chloride monomer.",
    "Properties: Durable, chemical resistant, and flexible.",
    "Applications: Pipes, cable insulation, and packaging materials.",
    "",
    "1. h) What is Co-polymerization? (2M, CO4, L1)",
    "Co-polymerization is the process of polymerizing two or more different monomers to form a copolymer, which combines the properties of the constituent monomers.",
    "",
    "1. i) Write the Beer-Lambert Law (2M, CO5, L3)",
    "Beer-Lambert law states that the absorbance (A) of a solution is directly proportional to the concentration (c) of the absorbing species and the path length (l):",
    "A = εcl",
    "where ε is the molar absorptivity.",
    "",
    "1. j) Principle of Chromatography (2M, CO5, L3)",
    "Chromatography is based on the differential distribution of compounds between a stationary phase and a mobile phase.",
    "As the mobile phase moves through the stationary phase, compounds in the mixture separate based on their interactions with the stationary phase."
]

for line in content:
    pdf.cell(200, 10, txt=line, ln=True)

# Save the pdf with name .pdf
output_path = "/mnt/data/Chemistry_Short_Answers_Part2.pdf"
pdf.output(output_path)

output_path

