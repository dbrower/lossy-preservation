library(tidyverse)

file_names <- c("output_0.05.csv","output_0.1.csv","output_0.2.csv","output_0.3.csv","output_0.4.csv","output_0.5.csv", "output_0.6.csv", "output_0.7.csv", "output_0.8.csv", "output_0.9.csv" , "output_0.95.csv"
                , "output_0.975.csv", "output_0.98.csv", "output_0.99.csv", "output_1.csv")

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

combined_graph <- wrap_plots(graph_list, nrow = 5, ncol = 3)

print(combined_graph)
