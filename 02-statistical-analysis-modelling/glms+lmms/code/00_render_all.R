
# helper script to render all files in parent directory directory:

for (file in list.files("02-statistical-analysis-modelling/glms+lmms/code/", pattern = "*.rmd")){ # loop over all files
  # render manually to specify output_dir
  rmarkdown::render(paste0("02-statistical-analysis-modelling/glms+lmms/code/", file), output_dir = "02-statistical-analysis-modelling/glms+lmms/")
}
  
