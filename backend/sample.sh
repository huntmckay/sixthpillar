# sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from macrocycle'
# echo ""
# echo "---"
# echo ""
# sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from mesocycle'
# echo ""
# echo "---"
# echo ""
# sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from microcycle'
# echo ""
# echo "---"
# echo ""
# sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from tracker'

sqlite3 -cmd '.headers on' -cmd '.mode markdown' database.db 'select * from exercise'

echo "You should add this to bash source so you can type it anywhere in the env"
