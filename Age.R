library(tidyverse)

file_names <- c("output_file_1.csv", "output_file_2.csv", "output_file_3.csv",
                "output_file_4.csv", "output_file_5.csv", "output_file_6.csv",
                "output_file_7.csv", "output_file_8.csv", "output_file_9.csv",
                "output_file_10.csv", "output_file_11.csv","output_file_12.csv",
                "output_file_13.csv", "output_file_14.csv","output_file_15.csv",
                "output_file_16.csv", "output_file_17.csv","output_file_18.csv",
                "output_file_19.csv","output_file_20.csv")

graph_list <- list()

for (file_name in file_names) {
  # Read the CSV file
  df <- read.csv(file_name, skip = 4)
  
  df$state <- case_when(
    df$state == "M" ~ "0",
    df$state == "H" ~ "1",
    TRUE ~ as.character(df$state)
  )

    
  df <- df %>% mutate(total_hits = cumsum(state))
  df <- df %>% mutate(hit_rate = cummean(state))
  df$access_time <- ymd_hms(df$access_time)
  
  graph <- df %>%
    mutate(access_time = ymd_hms(access_time),
           year = year(access_time)) %>%
    group_by(year) %>%
    summarise(min_hit_rate = min(hit_rate)) %>%
    ggplot(aes(x = year, y = min_hit_rate)) +
    geom_point() +
    geom_smooth() +
    labs(title = file_name)  
  
  graph_list[[file_name]] <- graph
}

library(patchwork)

combined_graph <- wrap_plots(graph_list, nrow = 3, ncol = 7)

print(combined_graph)
