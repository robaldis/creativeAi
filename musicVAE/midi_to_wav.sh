echo "usage: . fluid.sh <midi filename>"


find songs | while IFS= read -r f; do
    echo "$d"
    fluidsynth -F $f.wav $f
done

# for f in /songs/*.midi; do
#     echo $f
#     fluidsynth -F $f.wav $f
# done
