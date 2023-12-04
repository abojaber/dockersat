FROM mcr.microsoft.com/dotnet/sdk:6.0 as build
COPY ./code ./src

WORKDIR /src
RUN dotnet restore 

RUN dotnet build -o /app
RUN dotnet publish -o /publish

#RUN dotnet publish -c Release -o out
ENTRYPOINT ["dotnet", "run"]
# FROM mcr.microsoft.com/dotnet/sdk:6:0 as base
# COPY --from=build  /publish /app
# WORKDIR /app
# #EXPOSE 80
# CMD ["./myWebApp"]