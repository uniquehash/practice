/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: obelange <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2016/11/10 19:14:48 by obelange          #+#    #+#             */
/*   Updated: 2016/11/10 19:30:49 by obelange         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <stdio.h>
#include <stdarg.h>
#include <string.h>





int	variadic_one(char* format, ...)
{
	va_list arg_list;
	int x = 0;

	va_start(arg_list, format);
	x = va_arg(arg_list, int);
	printf("x: %i", x);
	va_end(arg_list);

	return (1);
}


int	main()
{
	int a = 10;

	variadic_one("help", a);


	return (0);
}
