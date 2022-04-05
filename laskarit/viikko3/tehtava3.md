```mermaid
sequenceDiagram
	main->>machine: Machine()
	machine-->tank: FuelTank()
	machine-->tank: fill(40)
	machine-->engine: Engine(tank)
	
