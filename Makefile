# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adidion <adidion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/03 14:26:01 by adidion           #+#    #+#              #
#    Updated: 2022/11/04 15:41:48 by adidion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all:
	@echo Setting up virtual env
	python3 -m pip install virtualenv
	python3 -m venv .venv
	( \
		source .venv/bin/activate; \
		python3 -m pip install -r ./requirements.txt; \
	)

clean:
	( \
	rm -rf .venv/;\
    )
