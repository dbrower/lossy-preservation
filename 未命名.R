# Load the required packages
library(ggplot2)
library(dplyr)
library(lubridate)
library(scales)

# Read the CSV file
df <- read.csv("output_data.csv", skip = 3)

df$state <- case_when(
  df$state == "M" ~ "0",
  df$state == "H" ~ "1",
  TRUE ~ as.character(df$state)
)

# adding new column called total hits
df <- df %>% mutate(total_hits = cumsum(state))
# Adding new column which gets the percentage of hit
df <- df %>% mutate(hit_rate = cummean(state))
df$access_time <- ymd_hms(df$access_time)

ggplot(data = df, aes(x = access_time, y = hit_rate)) + geom_point()

# minimum total hit group by year
df |>
  mutate(access_time = ymd_hms(access_time),
         year = year(access_time)) |>
  group_by(year) |>
  summarise(min_total_hits = min(total_hits)) |>
  ggplot(aes(x = year, y = min_total_hits)) +
  geom_point() +
  geom_smooth()

# minimum hit rate group by year
df |>
  mutate(access_time = ymd_hms(access_time),
         year = year(access_time)) |>
  group_by(year) |>
  summarise(min_hit_rate = min(hit_rate)) |>
  ggplot(aes(x = year, y = min_hit_rate)) +
  geom_point() +
  geom_smooth()



# total number of H and M for each year
df |>
  mutate(access_time = ymd_hms(access_time),
         year = year(access_time)) |>
  group_by(year, state) |>
  summarize(n_state = n()) |>
  ggplot(aes(x = year, y = n_state, color = state)) +
  geom_point() +
  geom_smooth()

# H and M scatter plot for each access time
df$state <- as.numeric(df$state)

df$access_time <- ymd_hms(df$access_time)

ggplot(data = df, aes(x = access_time, y = state)) +
  geom_point()

x_data_type <- class(df$access_time)
print(x_data_type)

# first 100 access time and their H or M 
df |>
  mutate(access_time = ymd_hms(access_time),
         state = ifelse(state == "M", 0, 1)) |>
  top_n(100, access_time) |>
  ggplot(aes(x = access_time, y = state)) +
  geom_point()

df |>
  mutate(access_time = ymd_hms(access_time),
         year = year(access_time)) |>
  group_by(year, state) |>
  summarize(n_state = n()) |>
  ggplot(aes(x = year, y = n_state, color = state)) +
  geom_line()


