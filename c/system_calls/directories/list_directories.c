/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list_directories.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: obelange <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/01/04 19:40:54 by obelange          #+#    #+#             */
/*   Updated: 2017/01/04 19:40:56 by obelange         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <dirent.h>
#include <stdio.h>


int	main (void)
{	

	DIR				*dirA;
	struct dirent	*fileA;
	char 			*labelA;

	labelA = "test";
	dirA = opendir(".");
	// fileA = readdir(dirA);


	while ((fileA = readdir(dirA)) > 0)
	{
		// printf("file &: %p\n", fileA);
		// printf("file name: %s\n", fileA->d_name);	
		// printf("file name &: %p\n\n", fileA->d_name);
		printf("%s\n", fileA->d_name);
	}
	






	return (0);
}