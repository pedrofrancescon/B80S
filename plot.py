import matplotlib.pyplot as plt
import numpy as np

# graph = [1, 0, -1, 1, -1, 0, 0, 1]
# wMessage = "Mensagem Escrita"
# bMessage = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
# rMessage = "Resultado"

def ploting(graph, wMessage, bMessage, rMessage, client):

	if(client):
		binary = str()
		result = str()

		for i in range(len(bMessage)):
			binary += str(bMessage[i])

		for i in range(len(rMessage)):
			result += str(rMessage[i])

		plt.title('Mensagem: {}, Binario: {}, Saida: {}'.format(wMessage, binary, result))

	else:
		received = str()
		decoded = str()
		message = str()

		for i in range(len(wMessage)):
			received += str(wMessage[i])

		for i in range(len(bMessage)):
			decoded += str(bMessage[i])

		for i in range(len(rMessage)):
			message += str(rMessage[i])

		plt.title('Recebida: {}, Binario: {}, Mensagem: {}'.format(received, decoded, message))

	# plt.title('Escrita: {}\nBinario: {}\nSaida: {}\n'.format(wMessage, bMessage, rMessage))

	plt.step(graph, 'b')
	plt.ylabel('Polaridade')
	plt.xlabel('Tempo')
	mng = plt.get_current_fig_manager()
	mng.window.state("zoomed")


	# plt.show()

	plt.show(block=False)
	plt.pause(3)
	plt.close()